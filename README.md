# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 412
- HTTP: 250 alive / 82 gold
- HTTPS: 167 alive / 25 gold
- SOCKS4: 199 alive / 151 gold
- SOCKS5: 231 alive / 154 gold

## Historical pool

- Discovered: 154657
- Ever alive: 28911
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
