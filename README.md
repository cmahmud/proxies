# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 534
- HTTP: 443 alive / 176 gold
- HTTPS: 322 alive / 58 gold
- SOCKS4: 239 alive / 151 gold
- SOCKS5: 212 alive / 149 gold

## Historical pool

- Discovered: 125702
- Ever alive: 19685
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
