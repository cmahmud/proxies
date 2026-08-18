# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 244
- HTTP: 191 alive / 26 gold
- HTTPS: 167 alive / 9 gold
- SOCKS4: 181 alive / 106 gold
- SOCKS5: 210 alive / 103 gold

## Historical pool

- Discovered: 95258
- Ever alive: 10223
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
