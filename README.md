# SyndProxy validated proxy pool

## Current pool

- Alive now: 675
- Gold now: 402
- HTTP: 142 alive / 77 gold
- HTTPS: 195 alive / 25 gold
- SOCKS4: 163 alive / 145 gold
- SOCKS5: 175 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39983
- Ever gold: 1305

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
