# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 420
- HTTP: 113 alive / 70 gold
- HTTPS: 150 alive / 19 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41224
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
