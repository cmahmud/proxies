# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 410
- HTTP: 342 alive / 85 gold
- HTTPS: 228 alive / 26 gold
- SOCKS4: 231 alive / 146 gold
- SOCKS5: 268 alive / 153 gold

## Historical pool

- Discovered: 156427
- Ever alive: 29526
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
