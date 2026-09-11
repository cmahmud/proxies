# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 340
- HTTP: 151 alive / 78 gold
- HTTPS: 87 alive / 30 gold
- SOCKS4: 115 alive / 55 gold
- SOCKS5: 283 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48572
- Ever gold: 1545

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
