# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 397
- HTTP: 111 alive / 61 gold
- HTTPS: 60 alive / 16 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 190 alive / 163 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33650
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
