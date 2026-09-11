# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 423
- HTTP: 101 alive / 66 gold
- HTTPS: 55 alive / 19 gold
- SOCKS4: 186 alive / 166 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48899
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
