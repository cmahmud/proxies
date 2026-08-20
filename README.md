# SyndProxy private pool

## Current pool

- Alive now: 782
- Gold now: 385
- HTTP: 211 alive / 75 gold
- HTTPS: 158 alive / 16 gold
- SOCKS4: 203 alive / 147 gold
- SOCKS5: 210 alive / 147 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26413
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
