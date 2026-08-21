# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 413
- HTTP: 236 alive / 92 gold
- HTTPS: 172 alive / 21 gold
- SOCKS4: 194 alive / 147 gold
- SOCKS5: 220 alive / 153 gold

## Historical pool

- Discovered: 152161
- Ever alive: 27850
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
