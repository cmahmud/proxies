# SyndProxy private pool

## Current pool

- Alive now: 1291
- Gold now: 443
- HTTP: 491 alive / 109 gold
- HTTPS: 301 alive / 34 gold
- SOCKS4: 230 alive / 137 gold
- SOCKS5: 269 alive / 163 gold

## Historical pool

- Discovered: 159266
- Ever alive: 30365
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
