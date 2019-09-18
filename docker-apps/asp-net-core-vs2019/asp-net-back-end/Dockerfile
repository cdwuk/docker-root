FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["asp-net-vs2019/asp-net-vs2019.csproj", "asp-net-vs2019/"]
RUN dotnet restore "asp-net-vs2019/asp-net-vs2019.csproj"
COPY . .
WORKDIR "/src/asp-net-vs2019"
RUN dotnet build "asp-net-vs2019.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "asp-net-vs2019.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "asp-net-vs2019.dll"]