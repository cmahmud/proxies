# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 469
- HTTP: 154 alive / 101 gold
- HTTPS: 122 alive / 36 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45155
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
