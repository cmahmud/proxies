# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 446
- HTTP: 110 alive / 80 gold
- HTTPS: 113 alive / 32 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45632
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
