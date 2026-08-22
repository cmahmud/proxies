# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 413
- HTTP: 229 alive / 91 gold
- HTTPS: 184 alive / 30 gold
- SOCKS4: 218 alive / 140 gold
- SOCKS5: 240 alive / 152 gold

## Historical pool

- Discovered: 162770
- Ever alive: 31637
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
