# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 423
- HTTP: 103 alive / 74 gold
- HTTPS: 47 alive / 24 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49458
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
