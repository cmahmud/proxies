# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 385
- HTTP: 243 alive / 75 gold
- HTTPS: 174 alive / 16 gold
- SOCKS4: 217 alive / 146 gold
- SOCKS5: 213 alive / 148 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26465
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
