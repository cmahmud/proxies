# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 445
- HTTP: 120 alive / 75 gold
- HTTPS: 142 alive / 39 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 199 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44688
- Ever gold: 1410

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
