# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 444
- HTTP: 121 alive / 82 gold
- HTTPS: 137 alive / 34 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44722
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
