# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 445
- HTTP: 141 alive / 88 gold
- HTTPS: 80 alive / 33 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 216 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44211
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
