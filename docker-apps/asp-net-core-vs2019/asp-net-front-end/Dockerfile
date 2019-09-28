FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["asp-net-front-end.csproj", "asp-net-front-end/"]
RUN dotnet restore "asp-net-front-end/asp-net-front-end.csproj"
COPY . .
WORKDIR "/src/asp-net-front-end"
RUN dotnet build "asp-net-front-end.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "asp-net-front-end.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "asp-net-front-end.dll"]