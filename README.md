# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 389
- HTTP: 100 alive / 49 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33548
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
