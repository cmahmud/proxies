# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 422
- HTTP: 104 alive / 74 gold
- HTTPS: 45 alive / 25 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 174 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49458
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
