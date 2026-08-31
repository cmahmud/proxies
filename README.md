# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 480
- HTTP: 139 alive / 104 gold
- HTTPS: 132 alive / 39 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45093
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
