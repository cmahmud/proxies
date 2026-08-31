# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 482
- HTTP: 143 alive / 101 gold
- HTTPS: 116 alive / 45 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45068
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
