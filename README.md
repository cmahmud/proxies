# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 423
- HTTP: 95 alive / 76 gold
- HTTPS: 47 alive / 24 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 174 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49453
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
