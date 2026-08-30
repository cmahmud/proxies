# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 422
- HTTP: 111 alive / 74 gold
- HTTPS: 51 alive / 23 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44524
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
