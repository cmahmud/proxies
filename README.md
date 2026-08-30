# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 445
- HTTP: 117 alive / 74 gold
- HTTPS: 140 alive / 41 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44682
- Ever gold: 1410

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
