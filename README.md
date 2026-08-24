# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 385
- HTTP: 111 alive / 53 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 196 alive / 163 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33380
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
