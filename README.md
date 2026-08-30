# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 472
- HTTP: 132 alive / 95 gold
- HTTPS: 109 alive / 43 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 203 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44911
- Ever gold: 1418

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
