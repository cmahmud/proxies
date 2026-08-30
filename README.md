# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 420
- HTTP: 138 alive / 80 gold
- HTTPS: 76 alive / 30 gold
- SOCKS4: 160 alive / 150 gold
- SOCKS5: 259 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43879
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
