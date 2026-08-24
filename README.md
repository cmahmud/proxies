# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 390
- HTTP: 147 alive / 56 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 181 alive / 155 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33639
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
