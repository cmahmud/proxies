# SyndProxy validated proxy pool

## Current pool

- Alive now: 669
- Gold now: 494
- HTTP: 155 alive / 105 gold
- HTTPS: 141 alive / 49 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 200 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45003
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
