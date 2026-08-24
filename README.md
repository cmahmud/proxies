# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 392
- HTTP: 97 alive / 51 gold
- HTTPS: 44 alive / 16 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33397
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
