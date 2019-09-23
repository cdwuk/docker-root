FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["asp-net-back-end/asp-net-back-end.csproj", "asp-net-back-end/"]
RUN dotnet restore "asp-net-back-end/asp-net-back-end.csproj"
COPY . .
WORKDIR "/src/asp-net-back-end"
RUN dotnet build "asp-net-back-end.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "asp-net-back-end.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "asp-net-back-end.dll"]