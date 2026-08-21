# SyndProxy private pool

## Current pool

- Alive now: 932
- Gold now: 418
- HTTP: 300 alive / 109 gold
- HTTPS: 188 alive / 30 gold
- SOCKS4: 212 alive / 131 gold
- SOCKS5: 232 alive / 148 gold

## Historical pool

- Discovered: 160212
- Ever alive: 30633
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
