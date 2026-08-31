# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 469
- HTTP: 164 alive / 97 gold
- HTTPS: 121 alive / 36 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 224 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45308
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
