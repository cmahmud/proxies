# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 434
- HTTP: 308 alive / 96 gold
- HTTPS: 223 alive / 29 gold
- SOCKS4: 226 alive / 145 gold
- SOCKS5: 264 alive / 164 gold

## Historical pool

- Discovered: 158917
- Ever alive: 30126
- Ever gold: 1141

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
