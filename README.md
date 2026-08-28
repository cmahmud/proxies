# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 404
- HTTP: 94 alive / 61 gold
- HTTPS: 54 alive / 16 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42836
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
