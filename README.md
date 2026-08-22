# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 417
- HTTP: 228 alive / 94 gold
- HTTPS: 177 alive / 30 gold
- SOCKS4: 217 alive / 141 gold
- SOCKS5: 249 alive / 152 gold

## Historical pool

- Discovered: 162770
- Ever alive: 31640
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
