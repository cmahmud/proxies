# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 401
- HTTP: 96 alive / 64 gold
- HTTPS: 33 alive / 20 gold
- SOCKS4: 167 alive / 145 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48785
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
