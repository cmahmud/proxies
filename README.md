# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 414
- HTTP: 93 alive / 65 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 192 alive / 161 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48881
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
