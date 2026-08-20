# SyndProxy private pool

## Current pool

- Alive now: 680
- Gold now: 384
- HTTP: 194 alive / 73 gold
- HTTPS: 95 alive / 18 gold
- SOCKS4: 186 alive / 148 gold
- SOCKS5: 205 alive / 145 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25837
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
