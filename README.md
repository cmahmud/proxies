# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 454
- HTTP: 110 alive / 90 gold
- HTTPS: 128 alive / 29 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 221 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46559
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
