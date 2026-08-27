# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 407
- HTTP: 116 alive / 65 gold
- HTTPS: 178 alive / 14 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41146
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
