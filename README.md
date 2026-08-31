# SyndProxy validated proxy pool

## Current pool

- Alive now: 683
- Gold now: 470
- HTTP: 170 alive / 97 gold
- HTTPS: 117 alive / 38 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 221 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45307
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
