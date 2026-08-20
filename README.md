# SyndProxy private pool

## Current pool

- Alive now: 732
- Gold now: 375
- HTTP: 161 alive / 69 gold
- HTTPS: 183 alive / 21 gold
- SOCKS4: 203 alive / 148 gold
- SOCKS5: 185 alive / 137 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26200
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
