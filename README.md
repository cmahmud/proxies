# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 551
- HTTP: 354 alive / 172 gold
- HTTPS: 232 alive / 89 gold
- SOCKS4: 206 alive / 145 gold
- SOCKS5: 208 alive / 145 gold

## Historical pool

- Discovered: 124825
- Ever alive: 19160
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
