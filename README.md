# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 375
- HTTP: 83 alive / 48 gold
- HTTPS: 40 alive / 13 gold
- SOCKS4: 166 alive / 154 gold
- SOCKS5: 193 alive / 160 gold

## Historical pool

- Discovered: 172309
- Ever alive: 32966
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
