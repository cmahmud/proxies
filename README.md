# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 392
- HTTP: 307 alive / 85 gold
- HTTPS: 232 alive / 22 gold
- SOCKS4: 193 alive / 130 gold
- SOCKS5: 233 alive / 155 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24986
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
