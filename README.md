# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 422
- HTTP: 97 alive / 76 gold
- HTTPS: 49 alive / 23 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 174 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49452
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
