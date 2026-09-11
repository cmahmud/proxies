# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 419
- HTTP: 98 alive / 70 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 186 alive / 164 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48946
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
