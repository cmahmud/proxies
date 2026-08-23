# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 359
- HTTP: 136 alive / 37 gold
- HTTPS: 50 alive / 10 gold
- SOCKS4: 183 alive / 155 gold
- SOCKS5: 212 alive / 157 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32933
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
